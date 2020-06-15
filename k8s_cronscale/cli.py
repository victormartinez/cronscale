import click

import hpa
import settings


@click.group()
def main():
    pass


@main.command()
@click.option(
    "--project",
    required=True,
    type=click.Choice(settings.PROJECTS.keys()),
    help="Name of the onyo project hosted in cluster.",
)
@click.option("--min-replicas", required=True, type=click.INT, help="Min replicas.")
@click.option("--max-replicas", required=True, type=click.INT, help="Max replicas.")
def patch_hpa(project: str, min_replicas: int, max_replicas: int):
    """Update existing HorizontalPodAutoscaller of a given project.

    Usage:
        python cli.py patch-hpa --project onyo-backend --min 5 --max 10
    """
    return hpa.scale(project, min_replicas, max_replicas)


main.add_command(patch_hpa)


if __name__ == "__main__":
    main()
