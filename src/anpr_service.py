import fast_alpr
import os
import glob

def find_registration_plate(image_list: list[str]):
  alpr = fast_alpr.ALPR(
      detector_model="yolo-v9-t-384-license-plate-end2end",
      ocr_model="cct-xs-v1-global-model",
  )

  for image_name in image_list:
    prediction_result = alpr.predict(image_name)
    prediction = sorted(prediction_result, key=lambda x: x.ocr.confidence)[0] if prediction_result else None
    if prediction is not None and prediction.ocr.confidence > 0.95:
      return prediction.ocr.text
  return None
