To disable authentication in ngrok, you need to adjust your `ngrok` configuration file or start your tunnel without the `auth` option. Here are the steps to do so:

### Option 1: Using the Command Line

When starting your `ngrok` tunnel, omit the `auth` option. For example, instead of running:

```sh
ngrok http -auth="username:password" 80
```

Simply run:

```sh
ngrok http 80
```

### Option 2: Using the ngrok Configuration File

1. **Locate or Create the Configuration File:** The ngrok configuration file is typically located at `~/.ngrok2/ngrok.yml`. If it doesn't exist, you can create it.

2. **Edit the Configuration File:** Open the `ngrok.yml` file in a text editor and remove or comment out any `auth` settings.

For example, if your configuration file looks like this:

```yaml
authtoken: your_authtoken
tunnels:
  myapp:
    proto: http
    addr: 80
    auth: "username:password"
```

Change it to:

```yaml
authtoken: your_authtoken
tunnels:
  myapp:
    proto: http
    addr: 80
    # auth: "username:password"  # Comment out or remove this line
```

3. **Restart ngrok:** After saving the changes to your configuration file, restart your ngrok tunnel.

By following these steps, you should be able to disable authentication in ngrok. If you need any more assistance or specific details, feel free to ask!
