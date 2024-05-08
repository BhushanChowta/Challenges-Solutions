class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # Create a dictionary to store score and index pairs
        score_index = {}
        for i, s in enumerate(score):
            score_index[s] = i
        
        # Sort scores in descending order
        sorted_score = sorted(score, reverse=True)
        
        # Assign ranks
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i in range(len(sorted_score)):
            if i < 3:
                score_index[sorted_score[i]] = medals[i]
            else:
                score_index[sorted_score[i]] = str(i + 1)
        
        # Construct answer array
        answer = [score_index[score[i]] for i in range(len(score))]
        return answer
        