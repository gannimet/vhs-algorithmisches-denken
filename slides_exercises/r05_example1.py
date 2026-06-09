import datetime

def are_ranges_overlapping(start1, end1, start2, end2):
    if end1 < start2:
        return False
    
    if end2 < start1:
        return False
    
    return True


range1 = (datetime.date(2026, 6, 1), datetime.date(2026, 6, 30))
range2 = (datetime.date(2026, 6, 10), datetime.date(2026, 6, 15))

print(are_ranges_overlapping(range1[0], range1[1], range2[0], range2[1]))