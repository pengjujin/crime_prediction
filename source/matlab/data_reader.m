mapObj = containers.Map;
for i = 2:100000
    current_crime = Category{i};
    if(isKey(mapObj, current_crime))
        mapObj(current_crime) = mapObj(current_crime) + 1;
    else
        mapObj(current_crime) = 1;
    end
end