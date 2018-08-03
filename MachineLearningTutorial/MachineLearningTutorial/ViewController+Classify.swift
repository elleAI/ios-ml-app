//
//  ViewController+Classify.swift
//  MachineLearningTutorial
//
//  Created by Elena Jovcevska on 28.07.18.
//  Copyright © 2018 Elena Jovcevska. All rights reserved.
//

import UIKit

/// Extension of the ViewController, responsible for the classification
extension ViewController {
    
    func predictImageClass(_ image: UIImage) -> String? {
        let model = ObjectPredict()
        do {
            let category = try model.prediction(input_1: image.pixelBuffer(width: 200, height: 200)!)
            return category.classLabel
        } catch {
            print(error)
            return nil
        }
    }
}

