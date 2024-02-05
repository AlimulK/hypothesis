# Setup

First clone this repo.

Open the repo in the editor of your choice, I will be using VSCode.

## Setup Virtual Environment

### Create the Virtual Environment

Input into your terminal:

```commandline
python -m venv env
```

### Activating the Virtual Environment

Most of the time the environment will activate automatically (you may need to start a new terminal).

If it doesn't then type the following into the terminal:

```commandline
env\Scripts\activate
```

You should have `(env)` before the command prompt.

### Install the requirements

Input into your terminal:

```commandline
pip install -r requirements_user.txt
```

## Test that it works

Run `helloworld.py`

You should get a large output, the end of which should have:

```
UnboundLocalError: cannot access local variable 'character' where it is not associated with a value
Falsifying explicit example: test_decode_inverts_encode(
    s='',
)
```