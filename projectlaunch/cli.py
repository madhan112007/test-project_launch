"""
CLI - Simple GitHub Push Tool
"""
import click
from rich.console import Console
from projectlaunch.core import GitPusher

console = Console()


@click.group()
@click.version_option(version="1.0.0")
def main():
    """ProjectLaunch - Simple GitHub Push Tool"""
    pass


@main.command()
@click.option("--repo", "-r", help="GitHub repository URL")
@click.option("--message", "-m", help="Commit message")
@click.option("--path", "-p", default=".", help="Project path")
def push(repo, message, path):
    """Push your project to GitHub"""
    
    console.print("[bold cyan]ProjectLaunch - GitHub Push Tool[/bold cyan]\n")
    
    pusher = GitPusher(project_path=path)
    pusher.push_to_github(repo_url=repo, commit_message=message)


if __name__ == "__main__":
    main()
