//
//  ViewController+Layout.swift
//  MachineLearningTutorial
//
//  Created by Elena Jovcevska on 28.07.18.
//  Copyright © 2018 Elena Jovcevska. All rights reserved.
//

import Foundation

/// Extension of ViewController for the Layout of the UI elements
extension ViewController {
    
    func setupElementsVisibility(_ imageIsChosen: Bool) {
        self.imageContainer.isHidden = !imageIsChosen
        self.classifierLabel.isHidden = !imageIsChosen
        self.repeatButton.isHidden = !imageIsChosen
        self.startButton.isHidden = imageIsChosen
    }
}
