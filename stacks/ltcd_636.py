    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        cnt = [0] * n
        for log in logs:
            ID, action, time = log.split(':')
            ID = int(ID); time = int(time)
            if action == 'start':
                stack.append([ID,time])
            elif action == 'end':
                _, srt = stack.pop()
                add = time + 1 - srt
                cnt[ID] += add
                if stack:
                    cnt[stack[-1][0]] -= add

        return cnt
