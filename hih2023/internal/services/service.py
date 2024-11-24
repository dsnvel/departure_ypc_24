class ExecutionService:
    @staticmethod
    def get_meetings_by_tags(user_tags: list, tags: list, meetings: list):
        formed = {}
        for tag in tags:
            tag_id = str(tag['id'])
            tag_name = tag['name']
            for meeting in meetings:
                if tag_id in meeting['tags'] and tag_id in user_tags:
                    if formed.get(tag_name) is None:
                        formed[tag_name] = []
                    formed[tag_name].append(meeting)

        return formed
