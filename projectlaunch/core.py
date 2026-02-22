"""
Core - Simple GitHub Push
"""
import subprocess
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()


class GitPusher:
    """Simple Git push to GitHub."""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path).resolve()

    def push_to_github(self, repo_url: str = None, commit_message: str = None):
        """Push project to GitHub."""
        
        # Check if git repo exists and has remote
        existing_remote = None
        if (self.project_path / ".git").exists():
            try:
                existing_remote = self._run_git("remote", "get-url", "origin")
                console.print(f"[dim]Using existing remote: {existing_remote}[/dim]")
            except Exception:
                pass
        
        # Only ask for repo URL if not provided and no existing remote
        if not repo_url and not existing_remote:
            console.print("[cyan]Enter your GitHub repository URL:[/cyan]")
            repo_url = Prompt.ask("Repository URL")
        elif not repo_url:
            repo_url = existing_remote
        
        if not commit_message:
            console.print("[cyan]Enter commit message:[/cyan]")
            commit_message = Prompt.ask("Commit message", default="Update")
        
        console.print(Panel(f"[bold cyan]Pushing to GitHub...[/bold cyan]"))
        
        try:
            self._run_git("--version")
        except Exception:
            console.print("[red]Git not installed! Install from https://git-scm.com[/red]")
            return
        
        if not (self.project_path / ".git").exists():
            console.print("[cyan]Initializing git...[/cyan]")
            self._run_git("init", "-b", "main")
        
        console.print("[cyan]Adding files...[/cyan]")
        self._run_git("add", ".")
        
        console.print(f"[cyan]Committing: {commit_message}[/cyan]")
        try:
            self._run_git("commit", "-m", commit_message)
        except Exception as e:
            if "nothing to commit" in str(e):
                console.print("[yellow]No changes to commit[/yellow]")
        
        # Only set remote if it doesn't exist
        if not existing_remote:
            console.print("[cyan]Setting remote...[/cyan]")
            try:
                self._run_git("remote", "add", "origin", repo_url)
            except Exception:
                self._run_git("remote", "set-url", "origin", repo_url)
        
        console.print("[cyan]Pushing...[/cyan]")
        try:
            self._run_git("push", "-u", "origin", "main")
        except Exception:
            self._run_git("push", "-u", "origin", "main", "--force")
        
        console.print(Panel(
            f"[bold green]Successfully pushed![/bold green]\n\n"
            f"Repository: [cyan]{repo_url}[/cyan]",
            title="Success"
        ))
    
    def _run_git(self, *args):
        result = subprocess.run(
            ["git"] + list(args),
            cwd=str(self.project_path),
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip() or result.stdout.strip())
        return result.stdout.strip()
