class Main {
    static send_key(key) {
        if (!Spells.is_use_availability())
            return false

        SendInput key
        sleep Random(150, 200)
        return true
    }
}

; И тут правки