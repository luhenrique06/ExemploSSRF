#!/bin/bash

program_name="docker-compose"


if command -v "$program_name" >/dev/null 2>&1; then
  alias dc=docker-compose
else
  alias dc="docker compose"
fi


dc down && dc build && dc up