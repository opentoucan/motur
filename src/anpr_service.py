import fast_alpr
from typing import Optional
from fast_alpr import ALPRResult, OcrResult

def find_registration_plate(file_name: str) -> Optional[str]:
  alpr = fast_alpr.ALPR(
      detector_model="yolo-v9-t-384-license-plate-end2end",
      ocr_model="cct-xs-v1-global-model",
  )

  prediction_result = alpr.predict(file_name)

  for alprresult in prediction_result:
    if alprresult.ocr is None:
      break
    ocr_result: OcrResult = alprresult.ocr
    if type(ocr_result.confidence) is not float:
      break
    if ocr_result.confidence > 0.95:
      return ocr_result.text
  return None
