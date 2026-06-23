class Multicast {
    static use_1() {
        if ((PixelGetColor(977, 950) = "0x4E5865") || (PixelGetColor(1035, 950) = "0x4E5865")) {
            Spells.use("ice_wall")
        } else {
            Spells.use("ghost_walk")
        }

        Spheres.prepare("quas")
        return
    }

    static use_2() {
        if (Spells.is_preparation()) {
            Spells.prepare_multicast("sun_strike", "chaos_meteor", "deafening_blast")
        } else {
            Spells.prepare_multicast("sun_strike", "chaos_meteor")
            Spells.use_item 3
            Spells.use "sun_strike"
            Spells.use "chaos_meteor"
            Spells.use "deafening_blast"
            Spells.use "cold_snap"
            Spells.use_item 5
            Spells.prepare_multicast("sun_strike", "chaos_meteor", "deafening_blast")
        }

        return
    }

    static use_3() {
        if (Spells.is_preparation()) {
            Spells.prepare_multicast("cold_snap", "chaos_meteor", "deafening_blast")
        } else {
            Spells.prepare_multicast("cold_snap", "chaos_meteor")
            Spells.use "cold_snap"
            Spells.use "chaos_meteor"
            Spells.use "deafening_blast"
            Spells.use_item 3
            Spells.use_item 5
            Spells.prepare_multicast("cold_snap", "chaos_meteor", "deafening_blast")
        }

        return
    }

    static use_4() {
        if (Spells.is_preparation()) {
            Spells.prepare_multicast("tornado", "sun_strike", "chaos_meteor")
        } else {
            Spells.prepare_multicast("tornado", "sun_strike")
            Spells.use "tornado"
            sleep 1400
            Spells.use "sun_strike"
            Spells.use "chaos_meteor"
            sleep 1000
            Spells.use "deafening_blast"
            Spells.use "cold_snap"
            Spells.use_item 3
            Spells.use_item 5
            Spells.prepare_multicast("tornado", "sun_strike", "chaos_meteor")
        }

        return
    }
}