def solution(genres, plays):
    total = {}
    songs = {}
    answer = []
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        total[genre] = total.get(genre, 0) + play
        
        if genre not in songs:
            songs[genre] = []
        
        songs[genre].append((i, play))
    
    sorted_genres = sorted(
        total,
        key=lambda genre: total[genre],
        reverse=True
    )
    
    for genre in sorted_genres:
        sorted_songs = sorted(
            songs[genre],
            key=lambda song: (-song[1], song[0])
        )
        
        selected = sorted_songs[:2]
        
        for i in selected:
            answer.append(i[0])
        
    return answer