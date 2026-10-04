import unittest
from challenges.stage_5_multimodal import TimecodeEngine

class TestStage5Multimodal(unittest.TestCase):
    def test_timecode_conversion(self):
        engine = TimecodeEngine()
        ms = 3661500  # 1 hour, 1 minute, 1 second, 500 ms
        srt = engine.ms_to_srt_timecode(ms)
        self.assertEqual(srt, "01:01:01,500")

        parsed_ms = engine.srt_timecode_to_ms("01:01:01,500")
        self.assertEqual(parsed_ms, ms)

        # 60 frames at 30 fps = 2000 ms
        self.assertEqual(engine.frames_to_ms(60, fps=30.0), 2000)

if __name__ == "__main__":
    unittest.main()
