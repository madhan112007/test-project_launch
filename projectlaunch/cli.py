"""
CLI - Simple GitHub Push Tool
"""
import click
from rich.console import Console
from projectlaunch.core import GitPusher

console = Console()


@click.command()
@click.version_option(version="1.0.4")
@click.option("--repo", "-r", help="GitHub repository URL")
@click.option("--message", "-m", help="Commit message")
@click.option("--path", "-p", default=".", help="Project path")
def main(repo, message, path):
    """ProjectLaunch - Simple GitHub Push Tool"""
    
    console.print("[bold cyan]ProjectLaunch - GitHub Push Tool[/bold cyan]\n")
    
    pusher = GitPusher(project_path=path)
    pusher.push_to_github(repo_url=repo, commit_message=message)


if __name__ == "__main__":
    main()
