from pathlib import Path


class Point:
    """"""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class ImageRect:
    """"""

    def __init__(self, up_left_point: Point, down_right_point: Point) -> None:
        self.up_left_point = up_left_point
        self.down_right_point = down_right_point


def change_date(application_image_path: Path, date_image_rect: ImageRect) -> Path:
    """
    Change application date using base application template.

    Paramteres:
        application_image_path: Path - path to the basic application template.
        date_image_rect: ImageRect - rect of the date field in the image.

    Returns:
        result: Path - path to the faked image.
    """
    pass
