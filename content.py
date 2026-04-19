def perform_search(query):
    if not query:
        return []
        
    # This acts as our mock database.
    database = [
        {"title": "The Launch Event", "snippet": "On Saturday, April 4th, we proudly introduced EduLink to the student body at The Royal Academy."},
        {"title": "Campus Integration", "snippet": "EduLink was officially integrated directly into The Royal Academy's main school website."},
        {"title": "Community Traction", "snippet": "Our community has already grown to roughly 250 active users generating almost 120 posts."},
        {"title": "Platform Refactoring", "snippet": "We are currently undertaking a major refactoring of our framework, transitioning entirely to TypeScript."},
        {"title": "Newton's Phase", "snippet": "Rigzin and Pema Thinley will be spearheading the highly anticipated Newton's development phase."},
        {"title": "Earth Day Initiatives", "snippet": "Our upcoming content and feature roadmap will place a special thematic focus on Earth Day initiatives."}
    ]
    
    query = query.lower()
    
    results = [
        item for item in database
        if query in item['title'].lower() or query in item['snippet'].lower()
    ]
    
    return results