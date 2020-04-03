#!/bin/bash

echo "Starting Federated System."

x-terminal-emulator -e ./Server/server_start.sh

x-terminal-emulator -e ./Client/client_start.sh



$SHELL
