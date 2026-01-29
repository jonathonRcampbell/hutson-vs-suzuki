#!/usr/bin/env python3
"""
Fetch NHL player stats from the NHL API and save to stats.json
"""
import requests
import json
from datetime import datetime

# Player IDs
HUTSON_ID = "8483457"
SUZUKI_ID = "8480018"

def fetch_player_stats(player_id):
    """
    Fetch stats for a player from the NHL API
    """
    url = f"https://api-web.nhle.com/v1/player/{player_id}/landing"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Extract current season stats
        # The API returns stats in featuredStats.regularSeason.subSeason
        stats = data.get('featuredStats', {}).get('regularSeason', {}).get('subSeason', {})
        
        # If subSeason is empty, try career stats as fallback
        if not stats or stats.get('gamesPlayed', 0) == 0:
            stats = data.get('featuredStats', {}).get('regularSeason', {}).get('career', {})
        
        return {
            'games': stats.get('gamesPlayed', 0),
            'goals': stats.get('goals', 0),
            'assists': stats.get('assists', 0),
            'points': stats.get('points', 0)
        }
    except Exception as e:
        print(f"Error fetching stats for player {player_id}: {e}")
        return {
            'games': 0,
            'goals': 0,
            'assists': 0,
            'points': 0
        }

def main():
    """
    Main function to fetch stats and save to JSON
    """
    print("Fetching NHL stats...")
    
    hutson_stats = fetch_player_stats(HUTSON_ID)
    print(f"Hutson: {hutson_stats}")
    
    suzuki_stats = fetch_player_stats(SUZUKI_ID)
    print(f"Suzuki: {suzuki_stats}")
    
    # Create the stats object
    stats_data = {
        'hutson': hutson_stats,
        'suzuki': suzuki_stats,
        'lastUpdated': datetime.utcnow().isoformat() + 'Z'
    }
    
    # Save to stats.json
    with open('stats.json', 'w') as f:
        json.dump(stats_data, f, indent=2)
    
    print("Stats saved to stats.json")
    print(f"Last updated: {stats_data['lastUpdated']}")

if __name__ == "__main__":
    main()
