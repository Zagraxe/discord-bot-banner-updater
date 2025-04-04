# Discord Server Banner Updater

Automatically updates your Discord server's banner using a bot whenever the banner image is changed.

## Setup

1. **Add Secrets** to your GitHub repository:
   - `DISCORD_TOKEN`: Your bot's token.
   - `DISCORD_GUILD_ID`: The ID of your server.

2. **Replace the default banner image** in `assets/banner.png` with your own.

3. **Commit any changes** to `assets/banner.png`, `bot.py`, or the workflow to trigger the update.

## Files

- `bot.py`: Python script to upload the banner.
- `requirements.txt`: Required Python dependencies.
- `.github/workflows/update_banner.yml`: GitHub Actions workflow.
- `assets/banner.png`: Your banner image.

## Requirements

- A Discord bot with permissions to manage server settings.
- A valid banner image that follows Discord's specs.

## Notes

This repo is designed to be simple and reusable. Feel free to fork and use it in your own projects.
