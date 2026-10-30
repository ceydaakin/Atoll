import Foundation

@main
struct VolumeHUDIconRegression {
    static func main() {
        // AirPods connected but the sound goes to the speakers (#792): no headset icon.
        precondition(VolumeHUDIcon.headsetSymbol(connectedDeviceSymbol: "airpods", defaultOutputIsBluetooth: false) == nil)
        precondition(VolumeHUDIcon.headsetSymbol(connectedDeviceSymbol: "headphones", defaultOutputIsBluetooth: false) == nil)

        // The headset is the output: keep its icon.
        precondition(VolumeHUDIcon.headsetSymbol(connectedDeviceSymbol: "airpods", defaultOutputIsBluetooth: true) == "airpods")

        // Nothing connected: no headset icon whatever the route says.
        precondition(VolumeHUDIcon.headsetSymbol(connectedDeviceSymbol: nil, defaultOutputIsBluetooth: true) == nil)
    }
}
