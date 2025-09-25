# Note: Make function to show CANCELLED on bookings if the show is deleted.

"""def delete_show_and_cancel_bookings(show_id):
    show = session.query(Show).get(show_id)
    if show:
        for booking in show.bookings:
            booking.booking_status = BookingStatus.CANCELLED
        session.commit()
        session.delete(show)
        session.commit()"""