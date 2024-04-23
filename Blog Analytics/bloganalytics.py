import random

class BlogAnalytics:
    def __init__(self):
        self.visitors = {}
        self.page_views = {}
        self.comments = {}
    
    def track_visitor(self, user_id):
        if user_id in self.visitors:
            self.visitors[user_id] += 1
        else:
            self.visitors[user_id] = 1
    
    def track_page_view(self, page_url):
        if page_url in self.page_views:
            self.page_views[page_url] += 1
        else:
            self.page_views[page_url] = 1
    
    def track_comment(self, user_id):
        if user_id in self.comments:
            self.comments[user_id] += 1
        else:
            self.comments[user_id] = 1
    
    def generate_report(self):
        total_visitors = sum(self.visitors.values())
        total_page_views = sum(self.page_views.values())
        total_comments = sum(self.comments.values())
        
        print("Blog Analytics Report:")
        print("-----------------------")
        print("Total Visitors:", total_visitors)
        print("Total Page Views:", total_page_views)
        print("Total Comments:", total_comments)
        print("-----------------------")
        print("Top 5 Most Viewed Pages:")
        sorted_pages = sorted(self.page_views.items(), key=lambda x: x[1], reverse=True)
        for i, (page, views) in enumerate(sorted_pages[:5], 1):
            print(f"{i}. {page}: {views} views")
        print("-----------------------")
        print("Top 5 Most Active Users (by comments):")
        sorted_users = sorted(self.comments.items(), key=lambda x: x[1], reverse=True)
        for i, (user, comments) in enumerate(sorted_users[:5], 1):
            print(f"{i}. User {user}: {comments} comments")
    
    def simulate_activity(self, num_visitors, num_page_views, num_comments):
        for _ in range(num_visitors):
            user_id = random.randint(1, 100)
            self.track_visitor(user_id)
        
        for _ in range(num_page_views):
            page_url = f"/blog/post{random.randint(1, 20)}"
            self.track_page_view(page_url)
        
        for _ in range(num_comments):
            user_id = random.randint(1, 100)
            self.track_comment(user_id)

# Example usage
analytics = BlogAnalytics()
analytics.simulate_activity(1000, 5000, 200)
analytics.generate_report()
