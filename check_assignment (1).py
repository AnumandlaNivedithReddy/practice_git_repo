"""
SKYLINE HOTELS — SELF-CHECK / AUTO-GRADER
==========================================
Run it against your own file:

    python check_assignment.py            # checks skyline.py
    python check_assignment.py skyline    # same thing, explicit

It prints one line per check and a score out of 100. Nothing is hidden:
read the checks to understand exactly what each task expects.
"""

import sys
import traceback
from datetime import date

MODULE = sys.argv[1].removesuffix(".py") if len(sys.argv) > 1 else "skyline"

try:
    m = __import__(MODULE)
except Exception:
    print(f"Could not import '{MODULE}.py':\n")
    traceback.print_exc()
    sys.exit(1)

results: list[tuple[str, int, bool, str]] = []


def check(label: str, marks: int):
    def wrap(fn):
        try:
            fn()
            results.append((label, marks, True, ""))
        except AssertionError as exc:
            results.append((label, marks, False, str(exc) or "assertion failed"))
        except Exception as exc:
            results.append((label, marks, False, f"{type(exc).__name__}: {exc}"))
        return fn
    return wrap


def approx(a, b, tol=0.01):
    assert abs(a - b) < tol, f"expected {b}, got {a}"

# ---------------------------------------------------------------- TASK 1 (20)
@check("T1a Guest stores points privately (no public 'points' attribute set directly)", 5)
def _():
    g = m.Guest("G-999", "Test User", "9000000000", "t@example.com", "GOLD", 500)
    assert g.reward_points == 500
    assert not hasattr(g, "points") or g.reward_points == 500
    try:
        g.reward_points = 99_999
        assert g.reward_points == 500, "reward_points must be read-only"
    except AttributeError:
        pass


@check("T1b Guest.discount_rate maps the four loyalty tiers", 5)
def _():
    for tier, rate in [("PLATINUM", 0.15), ("GOLD", 0.10), ("SILVER", 0.05), ("NONE", 0.0)]:
        g = m.Guest("G-999", "T", "9", "t@e.com", tier, 0)
        approx(g.discount_rate, rate, 1e-9)


@check("T1c redeem_points refuses to overdraw and raises InsufficientPoints", 5)
def _():
    g = m.Guest("G-999", "T", "9", "t@e.com", "GOLD", 100)
    assert g.redeem_points(40) == 60
    try:
        g.redeem_points(1000)
        assert False, "overdraw was allowed"
    except m.InsufficientPoints:
        pass
    assert g.reward_points == 60


@check("T1d from_csv_row classmethod and mask_email staticmethod", 5)
def _():
    row = {"guest_id": "G-777", "name": "Row Guest", "phone": "9", "email": "row@e.com",
           "loyalty_tier": "SILVER", "reward_points": "300"}
    g = m.Guest.from_csv_row(row)
    assert isinstance(g, m.Guest) and g.reward_points == 300 and g.loyalty_tier == "SILVER"
    assert m.Guest.mask_email("nithya@example.com") == "n*****@example.com"


# ---------------------------------------------------------------- TASK 2 (15)
@check("T2a Room is abstract and cannot be instantiated", 5)
def _():
    try:
        m.Room("X", 1, 2, 3000)
        assert False, "abstract Room was instantiated"
    except TypeError:
        pass


@check("T2b Four room subclasses exist with correct room_type and inheritance chain", 5)
def _():
    assert m.StandardRoom.room_type == "STANDARD"
    assert m.DeluxeRoom.room_type == "DELUXE"
    assert m.Suite.room_type == "SUITE"
    assert m.Penthouse.room_type == "PENTHOUSE"
    assert issubclass(m.Penthouse, m.Room) and issubclass(m.Suite, m.Room)


@check("T2c amenities() grows down the hierarchy via super()", 5)
def _():
    std = set(m.StandardRoom("1", 1, 2, 3200).amenities())
    pent = set(m.Penthouse("4", 4, 6, 18500).amenities())
    assert std < pent, "Penthouse amenities must be a superset of Standard's"
    assert len(pent) >= len(std) + 4


# ---------------------------------------------------------------- TASK 3 (20)
@check("T3a nightly_rate applies the season multiplier", 5)
def _():
    r = m.DeluxeRoom("201", 2, 3, 5400)
    approx(r.nightly_rate("PEAK"), 7290.00)
    approx(r.nightly_rate("SHOULDER"), 5400.00)
    approx(r.nightly_rate("OFF"), 4320.00)


@check("T3b extra_guest_fee: 12% of base per guest over two; Suite/Penthouse charge nothing", 5)
def _():
    approx(m.StandardRoom("103", 1, 3, 3600).extra_guest_fee(3), 432.00)
    approx(m.DeluxeRoom("203", 2, 4, 5900).extra_guest_fee(4), 1416.00)
    approx(m.StandardRoom("101", 1, 2, 3200).extra_guest_fee(2), 0.0)
    approx(m.Suite("301", 3, 4, 9800).extra_guest_fee(4), 0.0)
    approx(m.Penthouse("401", 4, 6, 18500).extra_guest_fee(6), 0.0)


@check("T3c airport_pickup_fee is 1800 except Penthouse, which is complimentary", 5)
def _():
    approx(m.StandardRoom("101", 1, 2, 3200).airport_pickup_fee(), 1800.0)
    approx(m.Suite("301", 3, 4, 9800).airport_pickup_fee(), 1800.0)
    approx(m.Penthouse("401", 4, 6, 18500).airport_pickup_fee(), 0.0)


@check("T3d gst_rate is 12% up to base 7500, 18% above", 5)
def _():
    approx(m.DeluxeRoom("201", 2, 3, 5400).gst_rate(), 0.12, 1e-9)
    approx(m.Suite("301", 3, 4, 9800).gst_rate(), 0.18, 1e-9)


# ---------------------------------------------------------------- TASK 4 (20)
def _booking(**kw):
    defaults = dict(
        booking_id="BK-TEST",
        guest=m.Guest("G-501", "Nithya Sharma", "9", "n@e.com", "PLATINUM", 12400),
        room=m.Suite("301", 3, 4, 9800),
        check_in=date(2026, 12, 24), check_out=date(2026, 12, 28),
        guests_count=4, season="PEAK", breakfast=True, airport_pickup=True,
    )
    defaults.update(kw)
    return m.Booking(**defaults)


@check("T4a nights is derived, not stored", 5)
def _():
    assert _booking().nights == 4


@check("T4b invoice() reproduces BK-8013 exactly", 5)
def _():
    inv = _booking().invoice()
    approx(inv["room_charge"], 52920.00)
    approx(inv["extras"], 12200.00)
    approx(inv["loyalty_discount"], 7938.00)
    approx(inv["gst"], 10292.76)
    approx(inv["total"], 67474.76)


@check("T4c invoice() reproduces BK-8012 (Standard, OFF season, pickup, no breakfast)", 5)
def _():
    b = _booking(
        booking_id="BK-8012",
        guest=m.Guest("G-506", "Vikram Salunke", "9", "v@e.com", "SILVER", 2200),
        room=m.StandardRoom("101", 1, 2, 3200),
        check_in=date(2026, 11, 25), check_out=date(2026, 11, 26),
        guests_count=2, season="OFF", breakfast=False, airport_pickup=True,
    )
    approx(b.invoice()["total"], 4739.84)


@check("T4d validation: bad dates and over-capacity bookings are refused", 5)
def _():
    try:
        _booking(check_in=date(2026, 12, 28), check_out=date(2026, 12, 24))
        assert False, "check_out before check_in was accepted"
    except ValueError:
        pass
    try:
        _booking(guests_count=9)
        assert False, "over-capacity booking was accepted"
    except m.RoomUnavailable:
        pass


# ---------------------------------------------------------------- TASK 5 (10)
@check("T5a len(booking) returns nights; bookings compare by total", 5)
def _():
    small = _booking(booking_id="S", room=m.StandardRoom("101", 1, 2, 3200),
                     guests_count=2, breakfast=False, airport_pickup=False)
    big = _booking()
    assert len(big) == 4
    assert small < big
    assert max([small, big]) is big


@check("T5b str(booking) shows id, room type and money", 5)
def _():
    s = str(_booking())
    assert "BK-TEST" in s and "SUITE" in s and ("67,474" in s or "67474" in s), s


# ---------------------------------------------------------------- TASK 6/7 (15)
@check("T6a load_hotel() reads all three CSVs", 5)
def _():
    h = m.load_hotel()
    assert len(h.rooms) == 9, f"expected 9 rooms, got {len(h.rooms)}"
    assert len(h.guests) == 6, f"expected 6 guests, got {len(h.guests)}"
    assert len(h) == 15, f"len(hotel) should be 15 bookings, got {len(h)}"
    assert "BK-8009" in h and "BK-9999" not in h


@check("T6b Hotel revenue and revenue_by_room_type", 5)
def _():
    h = m.load_hotel()
    approx(h.revenue(), 468520.12, 0.05)
    rbt = h.revenue_by_room_type()
    assert list(rbt)[0] == "SUITE", f"highest-earning type should be SUITE, got {list(rbt)}"
    approx(rbt["PENTHOUSE"], 169549.77, 0.05)


@check("T6c occupancy_nights and top_guest", 5)
def _():
    h = m.load_hotel()
    assert h.occupancy_nights() == 34, f"expected 34 room-nights, got {h.occupancy_nights()}"
    guest, spend = h.top_guest()
    assert guest.name == "Nithya Sharma", f"expected Nithya Sharma, got {guest.name}"
    approx(spend, 192644.73, 0.05)


# ---------------------------------------------------------------- REPORT
if __name__ == "__main__":
    print(f"\nGrading '{MODULE}.py'\n" + "-" * 78)
    earned = total = 0
    for label, marks, ok, err in results:
        total += marks
        earned += marks if ok else 0
        mark = "PASS" if ok else "FAIL"
        print(f"[{mark}] {marks:>2}  {label}")
        if not ok:
            print(f"         -> {err}")
    print("-" * 78)
    print(f"SCORE: {earned} / {total}")
    if earned == total:
        print("All checks green. Submit it.")
    sys.exit(0 if earned == total else 1)
