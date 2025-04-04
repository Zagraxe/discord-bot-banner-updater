# Discord Bot Banner Updater

This project automatically updates your Discord bot's banner using a GitHub Actions workflow.

## Setup

1. **Add a secret** to your GitHub repository:
   - `DISCORD_TOKEN`: Your bot's token.

2. **Replace the default banner image** in `assets/IMG_20250404_030139.png` with your own PNG image.

3. **Commit any changes** to the banner image, `bot.py`, or the workflow file to trigger the update.

## Files

- `bot.py`: Python script that uploads the new banner to Discord.
- `.github/workflows/update_banner.yml`: GitHub Actions workflow to automate the update.
- `assets/IMG_20250404_030139.png`: Your banner image (PNG format).

## Requirements

- A valid banner image that meets Discord's specifications.

This repository is open-source and ready to be used by anyone.
