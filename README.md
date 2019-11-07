# cookiecutter-dl-work

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for deep learning research

## Usage

### Options

* `author_name`: your name
* `project_name`: your project name
* `project_description`: description of your project (this will be inserted to `README.md`)
* `jupyter_port`: a port to access JupyterLab running on a container
* `tensorboard_port`: a port to access TensorBoard running on a container

### Generate project and launch Docker container

Run following commands:

```bash
$ cookiecutter https://github.com/eqs/cookiecutter-dl-work
# cd to generated project dir
$ docker-compose build # (or docker-compose build --no-cache)
$ docker-compose up -d
```

Access following URLs from web browser:

* `localhost:<jupyter_port>`
* `localhost:<tensorboard_port>`

Happy deep learning!

