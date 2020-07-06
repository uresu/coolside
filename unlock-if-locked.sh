#!/bin/bash

AWAKESTATUS=`adb shell dumpsys power | grep "mWakefulness=" | xargs`
LOCKEDSTATUS=`adb shell dumpsys power | grep "mHoldingWakeLockSuspendBlocker" | xargs`

echo -e "AWAKESTATUS = $AWAKESTATUS"
echo -e "LOCKEDSTATUS = $LOCKEDSTATUS"

if [[ $AWAKESTATUS == *"Awake"* ]]; then
	echo "Setting AWAKE to true..."
	AWAKE="true"
else
	echo "Setting AWAKE to false..."
	AWAKE="false"

fi

if [[ $LOCKEDSTATUS == *"mHoldingWakeLockSuspendBlocker=false"* ]]; then
	echo "Setting LOCKED to true..."
        LOCKED="true"
else
	echo "Setting LOCKED to false..."
	LOCKED="FALSE"
fi

echo -e "AWAKE  = $AWAKE"
echo -e "LOCKED = $LOCKED"

if [[ $AWAKE == "false" ]]; then
        echo "Waking up..."
        adb shell input keyevent KEYCODE_WAKEUP
	sleep 1
fi

if [[ $LOCKED == "true" ]]; then
	echo "Unlocking..."
	adb shell input keyevent 82
	sleep 1
fi

