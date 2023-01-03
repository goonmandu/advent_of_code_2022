def zone_fully_overlaps(zone1, zone2):
    zone1_start = int(zone1.split("-")[0])
    zone1_end = int(zone1.split("-")[1])
    zone2_start = int(zone2.split("-")[0])
    zone2_end = int(zone2.split("-")[1])
    if zone1_start < zone2_start:
        return zone1_end >= zone2_end
    elif zone1_start > zone2_start:
        return zone1_end <= zone2_end
    return True


def zone_overlaps_at_all(zone1, zone2):
    zone1_start = int(zone1.split("-")[0])
    zone1_end = int(zone1.split("-")[1])
    zone2_start = int(zone2.split("-")[0])
    zone2_end = int(zone2.split("-")[1])
    return zone1_end >= zone2_start and zone1_start <= zone2_end


def main():
    with open("input.txt") as f:
        raw_cleanup = f.readlines()
    cleanup = [zone_pair.strip().split(",") for zone_pair in raw_cleanup]
    fully_overlapping_zones = 0
    partially_overlapping_zones = 0
    for zone_pair in cleanup:
        if zone_fully_overlaps(zone_pair[0], zone_pair[1]):
            fully_overlapping_zones += 1
        if zone_overlaps_at_all(zone_pair[0], zone_pair[1]):
            partially_overlapping_zones += 1
    print(f"{fully_overlapping_zones=}")
    print(f"{partially_overlapping_zones=}")


if __name__ == "__main__":
    main()