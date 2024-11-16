import click
import os
import json
import sys

import et_engine as et
engine = et.Engine()


def check_api_key():
    """check if the api key exists"""
    if "ET_ENGINE_API_KEY" not in os.environ:
        click.echo("Error: ET_ENGINE_API_KEY environment variable is not set.", err=True)
        sys.exit(1)


@click.group()
def batches():
    """Filesystem operations"""
    check_api_key()


@batches.command()
def list():
    """List all filesystems"""
    try:
        batch_list = engine.batches.list_batches()
        for b in batch_list:
            click.echo(b)
    except PermissionError as e: #used to be AuthenticationError from et_engine.errors
        click.echo(f"Authentication Error: {str(e)}", err=True)
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)


@batches.command()
def clear():
    """Delete a filesystem"""
    try:
        engine.batches.clear_batches()
        click.echo("Successfully cleared batches.")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

