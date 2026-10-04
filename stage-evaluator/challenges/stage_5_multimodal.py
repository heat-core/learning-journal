"""
Stage 5 Challenge: Multimodal Media & Creative AI
Gate 4 Focus: Timecode Translation, Video Frame Indexing (Project P4)
"""

class TimecodeEngine:
    """
    Converts between milliseconds, video frames (at given FPS) and SRT/VTT timecode format (HH:MM:SS,mmm).
    """
    @staticmethod
    def ms_to_srt_timecode(milliseconds: int) -> str:
        if milliseconds < 0:
            raise ValueError("Timecode must be non-negative")
        total_seconds = milliseconds // 1000
        ms = milliseconds % 1000
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d},{ms:03d}"

    @staticmethod
    def srt_timecode_to_ms(tc: str) -> int:
        parts = tc.replace(",", ":").split(":")
        if len(parts) != 4:
            raise ValueError("Invalid timecode format")
        h, m, s, ms = map(int, parts)
        return (h * 3600000) + (m * 60000) + (s * 1000) + ms

    @staticmethod
    def frames_to_ms(frames: int, fps: float = 30.0) -> int:
        return int((frames / fps) * 1000)
