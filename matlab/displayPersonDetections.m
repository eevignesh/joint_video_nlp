%% @brief: Display person detections of the video sampled at a certain rate
%
%  @paramters:
%  imgDir - directory of frames extracted from video
%  personDir - directory containing the person bounding box .mat file
%  shotNumber - the shot to display
%  NOTE: it is assumed that the shot file shots.output is present in the imageDir

function displayPersonDetections(imgDir, personDir, shotNum)

numBoxes = 2;

addpath('/scail/u/vigneshr/utilities/voc-release5/vis');
shotFile = [imgDir '/shot.output.txt' ];
fid = fopen(shotFile);
shotData = textscan(fid, '%s%d%d', 'Headerlines', 2, 'Delimiter', ',');
fclose(fid);

imageNames = shotData{1};
isShotChange = shotData{2};
shotNumber = shotData{3};

imageNames = imageNames(shotNumber==shotNum);
sampleRate = 16;

sampleDiff = round(numel(imageNames)/sampleRate);
finalFrame = min(numel(imageNames), sampleDiff*(sampleRate-1) + 1);

%% Show in a 4X4 plot 
% resize image to 200 X (...)
ctr = 1;
for i = 1:sampleDiff:finalFrame
  im = imread([imgDir '/' imageNames{i}]);
  [~, baseImagename, ~] = fileparts(imageNames{i});
  personFile = [personDir '/' baseImagename];
  try
    load(personFile);
  catch
    person_boxes = [];
  end
  [m,n] = size(im);
  im = imresize(im, round(200.0/m));
  subplot(4,4,ctr);
  if ~isempty(person_boxes)
    minBoxNum = min(size(person_boxes,1), numBoxes);
    showboxes(im, person_boxes(1:minBoxNum, 1:4));
  else
    imshow(im);
  end
  ctr = ctr + 1;
end
