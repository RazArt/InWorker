class Spheres {
    static _selected := {
        names: { 1: "", 2: "", 3: "" },
        count: { quas: 0, wex: 0, exort: 0 }
    }
    static _availability := { quas: false, wex: false, exort: false }
    static _preparation := false
    static _structures := {
        cold_snap: { quas: 3, wex: 0, exort: 0 },
        ghost_walk: { quas: 2, wex: 1, exort: 0 },
        ice_wall: { quas: 2, wex: 0, exort: 1 },
        emp: { quas: 0, wex: 3, exort: 0 },
        tornado: { quas: 1, wex: 2, exort: 0 },
        alacrity: { quas: 0, wex: 2, exort: 1 },
        deafening_blast: { quas: 1, wex: 1, exort: 1 },
        sun_strike: { quas: 0, wex: 0, exort: 3 },
        forge_spirit: { quas: 1, wex: 0, exort: 2 },
        chaos_meteor: { quas: 0, wex: 1, exort: 2 }
    }
    static _prepared_spellname := ""

    static _update() {
        coordinate := 971
        position := 1

        loop 12 {
            if (position = 4)
                break

            color := PixelGetColor(coordinate, 877) ; Наверхуw
            ;~ color := PixelGetColor(coordinate, 909)  ; Внизу

            if (color = "0x287AAF") {
                this._selected.names.%position% := "quas"
                position++
            } else if (color = "0x77387E") {
                this._selected.names.%position% := "wex"
                position++
            } else if (color = "0x92571C") {
                this._selected.names.%position% := "exort"
                position++
            }

            coordinate += 44
        }

        this._selected.count := { quas: 0, wex: 0, exort: 0 }
        for index, sphere_name in this._selected.names.OwnProps() {
            if (sphere_name != "")
                this._selected.count.%sphere_name%++
        }

        return true
    }

    static get_prepared_spellname() {
        this._update()

        for spellname, structure_array in this._structures.OwnProps() {
            if (this._selected.count.quas = structure_array.quas) &&
            (this._selected.count.wex = structure_array.wex) &&
            (this._selected.count.exort = structure_array.exort)
                return spellname
        }

        return ""
    }

    static prepare(spellname) {
        if (!Spells.is_use_availability())
            return false

        spellname := (spellname = "quas") ? "cold_snap" : spellname
        spellname := (spellname = "wex") ? "emp" : spellname
        spellname := (spellname = "exort") ? "sun_strike" : spellname

        if (this.get_prepared_spellname() = spellname)
            return true

        if (this._preparation)
            return false

        this._preparation := true

        if (!this._availability.quas)
            this._availability.quas := (PixelGetColor(767, 945) = "0x222827") ? true : false
        if (!this._availability.wex)
            this._availability.wex := (PixelGetColor(825, 945) = "0x222827") ? true : false
        if (!this._availability.exort)
            this._availability.exort := (PixelGetColor(883, 945) = "0x222827") ? true : false
        
        for sphere_name, sphere_count in this._structures.%spellname%.OwnProps() {
            if (sphere_count > 0) {
                if (this._availability.%sphere_name% = false) {
                    this._preparation := false
                    return false
                }
            }
        }

        temp_spheres_names := this._selected.names.Clone()

        loop 3 {
            temp_spheres_counts := { quas: 0, wex: 0, exort: 0 }
            difference := { quas: 0, wex: 0, exort: 0 }

            temp_spheres_names.DeleteProp(A_Index)
            for index, sphere_name in temp_spheres_names.OwnProps() {
                if (sphere_name != "")
                    temp_spheres_counts.%sphere_name%++
            }

            for sphere_name, value in difference.OwnProps() {
                difference.%sphere_name% := this._structures.%spellname%.%sphere_name% - temp_spheres_counts.%sphere_name%
                difference.%sphere_name% := (difference.%sphere_name% < 0) ? 0 : difference.%sphere_name%
            }

            if (A_Index = (difference.quas + difference.wex + difference.exort)) {
                for sphere_name, sphere_count in difference.OwnProps() {
                    loop sphere_count {
                        Main.send_key Config.key_binds.%sphere_name%
                    }
                }

                this._preparation := false
                return true
            }
        }

        this._preparation := false
        return true
    }
}
