class Spells {
    static _selected := { 1: 0, 2: 0 }
    static _invoke_cooldown := false

    static _update() {
        spells := {
            coordinates: { 1: 966, 2: 1024 },
            colors: {
                cold_snap: { 1: "0x132495", 2: "0x50556B" },
                ghost_walk: { 1: "0x050D20", 2: "0x3C4247" },
                ice_wall: { 1: "0xA8D0EC", 2: "0x7B8893" },
                emp: { 1: "0x2B0330", 2: "0x605269" },
                tornado: { 1: "0x022C4B", 2: "0x444E58" },
                alacrity: { 1: "0x341817", 2: "0x3F4247" },
                deafening_blast: { 1: "0x1B457C", 2: "0x4B5363" },
                sun_strike: { 1: "0xF2D56D", 2: "0x938C75" },
                forge_spirit: { 1: "0x233140", 2: "0x3F454A" },
                chaos_meteor: { 1: "0xAC5C05", 2: "0x564F4F" }
            }
        }

        for spell_position, coordinate in spells.coordinates.OwnProps() {
            spell_color := PixelGetColor(coordinate, 950)
            for spellname, colors_array in spells.colors.OwnProps() {
                if ((colors_array.1 = spell_color) || (colors_array.2 = spell_color)) {
                    this._selected.%spell_position% := spellname 
                    break
                }
            }
        }

        return true
    }

    static is_use_availability() {
        if (GetKeyState(Config.key_binds.actions_lock_1))
            return false

        if (GetKeyState(Config.key_binds.actions_lock_2))
            return false

        return true
    }

    static is_preparation() {
        return GetKeyState(Config.key_binds.preparation_cast_mode)
    }

    static use_invoke() {
        if (!this.is_use_availability())
            return false

        if ((PixelGetColor(1076, 950) != "0xF0A025"))
            return false

        Main.send_key Config.key_binds.invoke
        return true
    }

    static prepare(spellname) {
        if (!this.is_use_availability())
            return false

        if ((Spheres.prepare(spellname) = false) || (this.use_invoke() = false))
            return false

        return true
    }

    static prepare_multicast(spellname_1, spellname_2, spellname_3 := "") {
        if (!this.is_use_availability())
            return false

        this._update()

        if ((this._selected.1 = spellname_1) && (this._selected.2 = spellname_2)) ||
        ((this._selected.2 = spellname_1) && (this._selected.1 = spellname_2)) {
            if (spellname_3)
                Spheres.prepare(spellname_3)
            return
        } else if (this._selected.2 = spellname_1) {
            this.prepare(spellname_1)
            this.prepare(spellname_2)
            if (spellname_3)
                Spheres.prepare(spellname_3)
            return
        } else if (this._selected.2 = spellname_2) {
            this.prepare(spellname_2)
            this.prepare(spellname_1)
            if (spellname_3)
                Spheres.prepare(spellname_3)
            return
        } else if (this._selected.1 = spellname_1) {
            this.prepare(spellname_2)
            if (spellname_3)
                Spheres.prepare(spellname_3)
            return
        } else if (this._selected.1 = spellname_2) {
            this.prepare(spellname_1)
            if (spellname_3)
                Spheres.prepare(spellname_3)
            return
        } else {
            this.prepare(spellname_1)
            this.prepare(spellname_2)
            if (spellname_3)
                Spheres.prepare(spellname_3)
            return
        }

        return
    }

    static use(spellname) {
        if (!this.is_use_availability())
            return false

        this._update()

        if (this.is_preparation()) {
            if ((this._selected.1 = spellname)) {
                return true
            } else {
                return this.prepare(spellname)
            }
        } else {
            if (this._selected.1 = spellname) {
                Main.send_key "{Alt down}" Config.key_binds.spell_1 "{Alt up}" Config.key_binds.spell_1
                return true
            } else if (this._selected.2 = spellname) {
                Main.send_key "{Alt down}" Config.key_binds.spell_2 "{Alt up}" Config.key_binds.spell_2
                return true
            } else if (Spheres.get_prepared_spellname() = spellname) {
                if (this.use_invoke() = true) {
                    Main.send_key "{Alt down}" Config.key_binds.spell_1 "{Alt up}" Config.key_binds.spell_1
                    return true
                }
                return false
            } else if (this.prepare(spellname)) {
                Main.send_key "{Alt down}" Config.key_binds.spell_1 "{Alt up}" Config.key_binds.spell_1
                return true
            }
        }

        return false
    }

    static use_item(item_num) {
        if (!this.is_use_availability())
            return false

        Main.send_key Config.key_binds.item_%item_num%
        return
    }
}
