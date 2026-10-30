/*
 * Atoll (DynamicIsland)
 * Copyright (C) 2024-2026 Atoll Contributors
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 */

import Foundation

/// A Bluetooth headset that is only connected is not where the sound goes:
/// with AirPods nearby and the speakers selected, the volume HUD must keep the
/// speaker icon. Use the headset's symbol only while the default output is Bluetooth.
enum VolumeHUDIcon {
    static func headsetSymbol(connectedDeviceSymbol: String?, defaultOutputIsBluetooth: Bool) -> String? {
        guard defaultOutputIsBluetooth else { return nil }
        return connectedDeviceSymbol
    }
}
