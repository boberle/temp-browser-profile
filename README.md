# Browser with a temporary profile

## Usage

Run a browser with a temporary profile, like the `--temp-profile` for the Ubuntu edition of chromium.

**But why?** I use this in two ways:

- to test the web site I create in a clean environment
- as an alternative to the private mode

This script will create a temporary directory and use it as the profile directory for a browser.

By default, the temporary directory is empty, but you can copy a predefined profile directory with the `-p` or `--default-profile` option. I use this with a prepared profile containing an adblocker, so each time I run the browser with a temporary profile, I get an adblocker "pre-installed".  Here are the instructions (with Firefox):

```bash
mkdir /tmp/myprofile
firefox --profile /tmp/myprofile
# here, install the adblocker and close firefox
python3 tempbrowserprofile.py --default-profile /tmp/myprofile
```

The `/tmp/myprofile` profile will be copyied to a random temporary directory, which will be used as the profile.  The original `/tmp/myprofile` wil be left untouched.

You can of course put `myprofile` in a permanent location (not in `/tmp`) and create an alias for the last command in your `.bashrc`:

```
alias tff="setsid python3 /path/to/tempbrowserprofile.py --default-profile /path/to/profile"
```

## Using something else than Firefox

By the default, the values are for Firefox. You can use something else,
or you can choose a custom location for Firefox, with the following
options:

- `--executable`: the path to the executable files (`/path/to/firefox`,
  `path/to/chromium`, etc.),
- `--profile-option`: the option used to pass the custom profile directory. Enter `profile` for Firefox, or `user-data-dir=` for Chromium. Note the `=` at the end because `chromium` wants the option be passed with the format `--option=value` and not `--option value`.

So, for example:

```bash
python3 tempbrowserprofile.py \
   --executable /path/to/chromium \
   --profile-option user-data-dir= \
   -default-profile /path/to/default_chromium_profile
```

---

Bruno Oberle (http://boberle.com)

License: MIT
