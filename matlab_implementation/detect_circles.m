% Function to detect and highlight circles in an image
function highlightCirclesInImage(imagePath)

    % Step 1: Read the input image
    originalImage = imread(imagePath);
    
    % Step 2: Convert the image to grayscale
    grayImage = rgb2gray(originalImage);
    
    % Step 3: Apply edge detection to identify the edges in the image
    edgeImage = edge(grayImage, 'Canny');
    
    % Step 4: Use the Hough Transform to detect circles in the edge-detected image
    minRadius = 10; % Minimum radius of circles to be detected
    maxRadius = 100; % Maximum radius of circles to be detected
    sensitivity = 0.85; % Adjust this value to control the sensitivity of circle detection
    [centers, radii, ~] = imfindcircles(edgeImage, [minRadius, maxRadius], 'ObjectPolarity', 'bright', 'Sensitivity', sensitivity);
    
    % Step 5: Highlight the detected circles in the original image
    highlightedImage = originalImage;
    numCircles = size(centers, 1);
    for i = 1:numCircles
        center = centers(i, :);
        radius = radii(i);
        highlightedImage = insertShape(highlightedImage, 'circle', [center(1), center(2), radius], 'LineWidth', 3, 'Color', 'red');
    end
    
    % Display the result
    figure;
    subplot(1, 2, 1);
    imshow(originalImage);
    title('Original Image');
    subplot(1, 2, 2);
    imshow(highlightedImage);
    title('Detected Circles');
    
end


%  usage
imagePath = 'path/to/your/image.jpg'; % Replace with the actual image path

highlightCirclesInImage(imagePath);
