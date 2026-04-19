def perform_search(query):
    if not query:
        return []
        
    database = [
        {"title": "The Launch Event", "snippet": "On Saturday, April 4th, we introduced EduLink.", "url": "#the-launch"},
        {"title": "Campus Integration", "snippet": "EduLink is now on the main school website.", "url": "#integration"},
        {"title": "Community Traction", "snippet": "Our community has grown to 250 active users.", "url": "#community-traction"},
        {"title": "Platform Refactoring", "snippet": "Transitioning entirely to TypeScript.", "url": "#looking-ahead"}
    ]
    
    query = query.lower()
    return [item for item in database if query in item['title'].lower() or query in item['snippet'].lower()]