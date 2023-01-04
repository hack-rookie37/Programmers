def solution(m, musicinfos):
    sharps = {"C#": "c", "D#": "d", "F#": "f", "G#": "g", "A#": "a", "B#": "b"}

    def convert(melody):
        converted = []
        for i in range(len(melody)):
            if melody[i] == "#":
                converted[-1] += "#"
            else:
                converted.append(melody[i])

        return "".join([sharps[note] if note in sharps else note for note in converted])

    answer = ["(None)", 0]
    for music in musicinfos:
        start, end, name, sheet = music.split(",")

        # calculate playtime
        s = int(start[:2]) * 60 + int(start[3:])
        e = int(end[:2]) * 60 + int(end[3:])
        pt = e - s

        # arrange music length
        sheet = convert(sheet)
        L = len(sheet)
        if pt < L:
            sheet = sheet[:pt]
        else:
            q, r = divmod(pt, L)
            sheet = sheet * q + sheet[:r]

        m = convert(m)
        if m in sheet:
            if pt > answer[1]:
                answer = [name, pt]

    return answer[0]
