//
//  ViewController.swift
//  MachineLearningTutorial
//
//  Created by Elena Jovcevska on 27.07.18.
//  Copyright © 2018 Elena Jovcevska. All rights reserved.
//

import UIKit

/// View Controller presenting the selected image and its prediction
class ViewController: UIViewController, PhotoSelection {
    var photoHandler: PhotosLibraryHandler?
    @IBOutlet weak var classifierLabel: UILabel!
    @IBOutlet weak var imageContainer: UIImageView!
    @IBOutlet weak var startButton: UIButton!
    @IBOutlet weak var repeatButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        NotificationCenter.default.addObserver(self, selector: #selector(appMovedToForeground), name: Notification.Name.UIApplicationWillEnterForeground, object: nil)
    }
    
    @objc func appMovedToForeground() {
        if imageContainer.image == nil {
            configureUserActionSheet()
        }
    }
    
    func configureUserActionSheet() {
        setupElementsVisibility(false)
        if photoHandler == nil {
            photoHandler = PhotosLibraryHandler.init()
        }
        photoHandler?.delegate = self
    }
    
    // MARK: PhotoSelection method
    func didSelectPhoto(_ image: UIImage?) {
        if let image = image {
            self.setupElementsVisibility(true)
            self.imageContainer.image = image
            let predictedClass = self.predictImageClass(image)
            if let prediction = predictedClass {
                self.classifierLabel.text = prediction
            } else {
                self.classifierLabel.text = "An error happened. Try again"
            }
        } else {
            self.setupElementsVisibility(true)
        }
        self.dismiss(animated: true, completion: nil)
    }
    
    @IBAction func repeatProcess(_ sender: Any) {
        self.setupElementsVisibility(false)
        configureUserActionSheet()
        photoHandler?.openPhotos()
    }
    
    @IBAction func startProcess(_ sender: Any) {
        configureUserActionSheet()
        photoHandler?.presentAction(vc: self)
    }
}
