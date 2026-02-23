default:
    @just --list
    
setup:
    python3 scripts/setup_env.py

verify:
    gauge run specs/
