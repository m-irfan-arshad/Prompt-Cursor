#!/usr/bin/env python3
"""
README Update Script for DevOps Prompt Library

This script automatically updates the README.md file with:
- Total number of prompts
- Last updated date
- Repository statistics
- Recent changes
"""

import os
import glob
import datetime
from pathlib import Path

def count_prompts():
    """Count total number of prompt files in the repository."""
    prompt_files = []
    
    # Directories to scan for prompts
    directories = ['Planning', 'Development', 'Testing', 'Deployment', 'Maintenance', 'Documentation', 'Infrastructure Architect']
    
    for directory in directories:
        if os.path.exists(directory):
            # Count .md files in each directory (excluding README.md)
            md_files = glob.glob(f"{directory}/*.md")
            readme_files = glob.glob(f"{directory}/README.md")
            prompt_files.extend([f for f in md_files if f not in readme_files])
    
    return len(prompt_files)

def get_directory_stats():
    """Get statistics for each directory."""
    stats = {}
    directories = ['Planning', 'Development', 'Testing', 'Deployment', 'Maintenance', 'Documentation', 'Infrastructure Architect']
    
    for directory in directories:
        if os.path.exists(directory):
            md_files = glob.glob(f"{directory}/*.md")
            readme_files = glob.glob(f"{directory}/README.md")
            prompt_count = len([f for f in md_files if f not in readme_files])
            stats[directory] = prompt_count
        else:
            stats[directory] = 0
    
    return stats

def update_readme():
    """Update the README.md file with current statistics."""
    readme_path = "README.md"
    
    if not os.path.exists(readme_path):
        print("README.md not found!")
        return
    
    # Read current README
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Calculate statistics
    total_prompts = count_prompts()
    directory_stats = get_directory_stats()
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Update repository stats section
    stats_section = f"""## 📊 Repository Stats

- **Total Prompts**: {total_prompts}
- **Categories**: 7
- **Last Updated**: {current_date}
- **Contributors**: [To be updated]

### 📁 Directory Breakdown
"""
    
    for directory, count in directory_stats.items():
        emoji_map = {
            'Planning': '📋',
            'Development': '🛠️',
            'Testing': '🧪',
            'Deployment': '🚀',
            'Maintenance': '🔧',
            'Documentation': '📚',
            'Infrastructure Architect': '🏗️'
        }
        emoji = emoji_map.get(directory, '📁')
        stats_section += f"- **{emoji} {directory}**: {count} prompts\n"
    
    # Replace the stats section in README
    import re
    
    # Find and replace the stats section
    stats_pattern = r'## 📊 Repository Stats.*?(?=## |$)'
    new_stats_section = stats_section + '\n'
    
    if re.search(stats_pattern, content, re.DOTALL):
        content = re.sub(stats_pattern, new_stats_section, content, flags=re.DOTALL)
    else:
        # If stats section doesn't exist, add it before the Support section
        support_pattern = r'## 📞 Support'
        if re.search(support_pattern, content):
            content = re.sub(support_pattern, new_stats_section + '\n' + support_pattern, content)
    
    # Write updated README
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ README.md updated successfully!")
    print(f"📊 Total prompts: {total_prompts}")
    print(f"📅 Last updated: {current_date}")
    
    # Print directory breakdown
    print("\n📁 Directory Breakdown:")
    for directory, count in directory_stats.items():
        emoji_map = {
            'Planning': '📋',
            'Development': '🛠️',
            'Testing': '🧪',
            'Deployment': '🚀',
            'Maintenance': '🔧',
            'Documentation': '📚',
            'Infrastructure Architect': '🏗️'
        }
        emoji = emoji_map.get(directory, '📁')
        print(f"  {emoji} {directory}: {count} prompts")

def main():
    """Main function to run the update script."""
    print("🔄 Updating README.md with current repository statistics...")
    update_readme()
    print("\n🎉 Update complete!")

if __name__ == "__main__":
    main()
