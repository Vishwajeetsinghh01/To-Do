terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
    }
  }
}

provider "docker" {}

resource "docker_image" "todo_app" {
  name = "to-do-app"

  build {
    context = "/mnt/c/Users/Dell/OneDrive/Desktop/To-Do"
  }
}

resource "docker_container" "todo_container" {
  name  = "to-do-container"
  image = docker_image.todo_app.image_id

  ports {
    internal = 5000
    external = 5000
  }
}