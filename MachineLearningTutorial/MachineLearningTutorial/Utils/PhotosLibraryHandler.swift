//
//  ViewController.swift
//  MachineLearningTutorial
//
//  Created by Elena Jovcevska on 27.07.18.
//  Copyright © 2018 Elena Jovcevska. All rights reserved.
//

import UIKit
import Foundation

/// Protocol for handling the selection of photo from library
protocol PhotoSelection: NSObjectProtocol {
    func didSelectPhoto(_ image: UIImage?)
}


/// Object for handling the photo library actions 
class PhotosLibraryHandler: NSObject, UIImagePickerControllerDelegate, UINavigationControllerDelegate{
    
    private var viewController: UIViewController!
    weak var delegate: PhotoSelection?
    
    func presentAction(vc: UIViewController) {
        viewController = vc
        let alertController = UIAlertController(title: "Choose photo to guess its category", message: nil, preferredStyle: .alert)
        
        alertController.addAction(UIAlertAction(title: "Open Photos", style: .default, handler: { (alert:UIAlertAction!) -> Void in
            self.openPhotos()
        }))
        vc.present(alertController, animated: true, completion: nil)
    }
    
    func openPhotos() {
        if UIImagePickerController.isSourceTypeAvailable(.photoLibrary){
            let pickerVC = UIImagePickerController()
            pickerVC.delegate = self
            pickerVC.sourceType = .photoLibrary
            viewController.present(pickerVC,
                                   animated: true,
                                   completion: nil)
        }
    }

    //MARK: UIImagePickerControllerDelegate
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : Any]) {
        let selectedImage = info[UIImagePickerControllerOriginalImage] as? UIImage
        delegate?.didSelectPhoto(selectedImage)
        viewController.dismiss(animated: true, completion: nil)
    }
    
}
