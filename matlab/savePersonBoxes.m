% @brief: computes the person boxes in an image using a voc-person model

% @parameters:
% imname - name of the image
% outname - mat file in which the person boxes are saved
% isGrammar - should we load the grammar model
% numBoxes - number of boxes which need to be saved (however min thresh = -2.5)
% isSkip - if outname file exists, skip

function savePersonBoxes(imname, outname, isGrammar, numBoxes, isSkip)

if nargin<5
  isSkip = true;
end

if exist(outname, 'file') && isSkip
  fprintf('File already exists!\n');
  return;
end

% set  minimum thresh
minThresh = -2.5;

% voc-folder
addpath('/scail/u/vigneshr/utilities/voc-release5');
startup;

% load the person model
if (isGrammar)
  load('/scail/u/vigneshr/utilities/voc-release5/VOC2010/person_grammar_final.mat');
else
  load('/scail/u/vigneshr/utilities/voc-release5/VOC2010/person_final.mat');
end

im = imread(imname);

% find the person boxes
tic;
[~, person_boxes] = process(im, model, minThresh);
toc;

minNumPeople = min(numBoxes, size(person_boxes,1));

if ~isempty(person_boxes)
  person_boxes = person_boxes(1:minNumPeople, :);
else
  person_boxes = [];
end

save(outname, 'person_boxes');
