# Hutson vs Suzuki - NHL Points Tracker

A live tracker comparing Lane Hutson and Nick Suzuki's points for the Montreal Canadiens.

## How It Works

This site uses GitHub Actions to automatically fetch NHL stats every hour and save them to `stats.json`. The webpage reads from this JSON file, completely avoiding CORS issues.

## Setup Instructions

1. **Add the files to your repository:**
   - Replace `index.html` with the new version
   - Create `.github/workflows/update-stats.yml` (create the `.github/workflows/` directories if they don't exist)
   - Add `fetch_stats.py` to the root of your repository
   - Add `stats.json` to the root (this will be auto-generated, but you can add the placeholder version)

2. **Enable GitHub Actions:**
   - Go to your repository settings
   - Navigate to Actions → General
   - Under "Workflow permissions", select "Read and write permissions"
   - Click "Save"

3. **Trigger the first update:**
   - Go to the "Actions" tab in your repository
   - Click on "Update NHL Stats" workflow
   - Click "Run workflow" button
   - Select the main branch and click "Run workflow"

4. **Wait a moment:**
   - The workflow will fetch the latest stats and commit `stats.json`
   - GitHub Pages will automatically rebuild your site
   - Your site should now show live stats!

## How to Update Manually

You can manually trigger stats updates at any time:
1. Go to the "Actions" tab
2. Click "Update NHL Stats"
3. Click "Run workflow"

## Troubleshooting

- **Stats showing as 0**: The GitHub Action hasn't run yet. Manually trigger it.
- **"Stats file not found" error**: Make sure `stats.json` exists in the root of your repository and GitHub Pages has been rebuilt.
- **Workflow failing**: Check the Actions tab for error logs. The NHL API might be temporarily down.

## Customization

To track different players, edit `fetch_stats.py` and change the player IDs:
```python
HUTSON_ID = "8483457"  # Change this
SUZUKI_ID = "8480018"  # Change this
```

You can find player IDs by visiting NHL.com player pages and looking at the URL.
