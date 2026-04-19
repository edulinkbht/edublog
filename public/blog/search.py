def perform_search(query):
    if not query:
        return []
        
    database = [
        {"title": "The Launch Event", "snippet": "On Saturday, April 4th, we introduced EduLink.", "url": "/launch.py"},
        {"title": "Backstory Of EduLink", "snippet": "How EduLink actually started and evolved over time.", "url": "/backstory.py"},
        {"title": "EduLink And Growth", "snippet": "Our community has grown to more than before", "url": "/growth.py"},
        {"title": "Research", "snippet": "The latest findings and studies related to EduLink.", "url": "/research.py"}
    ]
    
    query = query.lower()
    return [item for item in database if query in item['title'].lower() or query in item['snippet'].lower()]