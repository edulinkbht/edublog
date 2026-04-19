def perform_search(query):
    if not query:
        return []
        
    # Mock database now includes "url" to redirect the user to the right section
    database = [
        {
            "title": "The Launch Event", 
            "snippet": "On Saturday, April 4th, we proudly introduced EduLink to the student body at The Royal Academy.",
            "url": "bht"
        },
        {
            "title": "Campus Integration", 
            "snippet": "EduLink was officially integrated directly into The Royal Academy's main school website.",
            "url": "#integration"
        },
        {
            "title": "Community Traction", 
            "snippet": "Our community has already grown to roughly 250 active users generating almost 120 posts.",
            "url": "#community-traction"
        },
        {
            "title": "Platform Refactoring", 
            "snippet": "We are currently undertaking a major refactoring of our framework, transitioning entirely to TypeScript.",
            "url": "#looking-ahead"
        },
        {
            "title": "Newton's Phase", 
            "snippet": "Rigzin and Pema Thinley will be spearheading the highly anticipated Newton's development phase.",
            "url": "#looking-ahead"
        },
        {
            "title": "Earth Day Initiatives", 
            "snippet": "Our upcoming content and feature roadmap will place a special thematic focus on Earth Day initiatives.",
            "url": "#looking-ahead"
        }
    ]
    
    query = query.lower()
    
    # Return items where the query matches either the title or the snippet
    results = [
        item for item in database
        if query in item['title'].lower() or query in item['snippet'].lower()
    ]
    
    return results