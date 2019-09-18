# cookiecutter-dl-work

## Usage

### Generate project

```bash
$ cookiecutter https://github.com/eqs/cookiecutter-dl-work
# cd to generated project dir
$ docker-compose build
$ docker-compose up -d
```

### Options

* `author_name`: your name
* `project_name`: your project name
* `project_description`: description of your project (this will be inserted to `README.md`)
* `jupyter_port`: a port to access JupyterLab running on a container
* `tensorboard_port`: a port to access TensorBoard running on a container

