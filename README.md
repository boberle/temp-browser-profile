# Firefox with a temporary profile

Run Firefox with a temporary profile, like the `--temp-profile` of chromium/chrome.

**But why?** I use this in two ways:

- to test the web site I create in a clean environment
- as an alternative to the private mode

This script will create a temporary directory and use it as the profile directory for Firefox.

By default, the temporary directory is empty, but you can copy a predefined profile directory with the `-p` or `--default-profile` option. I use this with a prepared profile containing an adblocker, so each time I run Firefox with a temporary profile, I get an adblocker "pre-installed".  Here are the instructions:

```bash
mkdir /tmp/myprofile
firefox --profile /tmp/myprofile
# here, install the adblocker and close firefox
python3 tempfirefox.py --default-profile /tmp/myprofile
```

The `/tmp/myprofile` profile will be copyied to a random temporary directory, which will be used as the profile.  The original `/tmp/myprofile` wil be left untouched.

You can of course put `myprofile` in a permanent location (not in `/tmp`) and create an alias for the last command in your `.bashrc`:

```
alias tff="setsid python3 /path/to/tempfirefox.py --default-profile /path/to/profile"
```

---

Bruno Oberle (http://boberle.com)

License: MIT
