%% @brief: get the person detections of the video
%
%  @paramters:
%  imageDir - directory of frames extracted from video
%  personDir - directory containing the person bounding box .mat file
%  shotNumber - the shot to display
%  NOTE: it is assumed that the shot file shots.output is present in the imageDir
%
%  @Outputs:
%  imageFile - list of files in the shot
%  finalFrame - list of the person box names in the shot

function [imageFile, personFile, numPerShot] = getPersonBoxes(imageDir, personDir, shotNum)

numBoxes = 2;

addpath('/scail/u/vigneshr/utilities/voc-release5/vis');
shotFile = [imageDir '/shot.output.txt' ];
fid = fopen(shotFile);
shotData = textscan(fid, '%s%d%d', 'Headerlines', 2, 'Delimiter', ',');
fclose(fid);

imageNames = shotData{1};
isShotChange = shotData{2};
shotNumber = shotData{3};

numPerShot = [];
if nargout >= 3
  numPerShot = zeros(max(shotData{3}),1);
  for i = 1:max(shotData{3})
    numPerShot(i) = sum(shotNumber==i);
  end
end

if shotNum==-1
  imageNames = imageNames;
else
  imageNames = imageNames(shotNumber==shotNum);
end

sampleDiff = 1;
finalFrame = numel(imageNames);

imageFile = cell(finalFrame, 1);
personFile = cell(finalFrame, 1);

for i = 1:sampleDiff:finalFrame
  imageFile{i} = [imageDir '/' imageNames{i}];
  [~, baseImagename, ~] = fileparts(imageNames{i});
  personFile{i} = [personDir '/' baseImagename];  
end
